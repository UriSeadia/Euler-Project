# Take the number 192 and multiply it by each of 1, 2, and 3:
# 192 × 1 = 192
# 192 × 2 = 384
# 192 × 3 = 576

# By concatenating each product we get the 1 to 9 pan-digital, 192384576. We will call 192384576 the concatenated product of 192 and (1,2,3)
#
# The same can be achieved by starting with 9 and multiplying by 1, 2, 3, 4, and 5, giving the pan-digital, 918273645,
# which is the concatenated product of 9 and (1,2,3,4,5).
#
# What is the largest 1 to 9 pan-digital 9-digit number that can be formed as the concatenated product of an integer with (1,2, ... , n) where n > 1?

import time


def is_pan_digital(num_as_str: str):
    set_of_str = set(num_as_str)

    return ('0' not in set_of_str) and (len(set_of_str) == 9)


def is_concatenated_product(num_as_str: str):
    multiplicand = 2
    char_count = 1
    multiplier = num_as_str[0]

    while char_count < 9:
        rest_of_number = num_as_str[char_count: len(num_as_str): 1]
        product_as_str = str(multiplicand * int(multiplier))

        if product_as_str == rest_of_number[0: len(product_as_str): 1]:
            multiplicand += 1
            char_count += len(product_as_str)
        elif char_count < 5:
            char_count += 1
            multiplier = num_as_str[0: char_count: 1]
        else:
            return False
    return True


def pan_digital_multiples():
    num = 987654320

    while True:
        if is_pan_digital(str(num)):
            if is_concatenated_product(str(num)):
                break
        num -= 1

    return num


def main():
    start = time.time()

    print(pan_digital_multiples())

    end = time.time()
    print('Seconds: ' + str(end - start))


main()
