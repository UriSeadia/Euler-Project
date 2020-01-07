# We shall say that an n-digit number is pan-digital if it makes use of all the digits 1 to n exactly once;
# for example, the 5-digit number, 15234, is 1 through 5 pan-digital.
#
# The product 7254 is unusual, as the identity, 39 × 186 = 7254, containing multiplicand, multiplier, and product is 1 through 9 pan-digital.
#
# Find the sum of all products whose multiplicand/multiplier/product identity can be written as a 1 through 9 pan-digital.
#
# HINT: Some products can be obtained in more than one way so be sure to only include it once in your sum.

import time


def get_pan_digital_product(multiplicand, multiplier):
    digits_list = []
    product = multiplicand * multiplier
    digits = str(multiplicand) + str(multiplier) + str(product)

    if len(digits) != 9 or '0' in digits:
        return 0

    for digit in digits:
        if digit in digits_list:
            return 0

        digits_list.append(digit)

    return product


def sum_of_pan_digital_products():
    result_set = set()

    for i in range(2, 99):
        for j in range(123, 4988):
            result_set.add(get_pan_digital_product(i, j))

    result = sum(result_set)
    print(sorted(result_set))

    return result


def main():
    start = time.time()

    print(sum_of_pan_digital_products())

    end = time.time()
    print('Seconds: ' + str((end - start)))


main()
