# If the numbers 1 to 5 are written out in words: one, two, three, four, five,
# then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.
#
# If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, how many letters would be used?
#
# NOTE: Do not count spaces or hyphens.
# For example, 342 (three hundred and forty-two) contains 23 letters and 115 (one hundred and fifteen) contains 20 letters.
# The use of "and" when writing out numbers is in compliance with British usage.


def get_1_to_9():
    result = 3 + 3 + 5 + 4 + 4 + 3 + 5 + 5 + 4
    return result


def get_10_to_19():
    result = 3 + 6 + 6 + 8 + 8 + 7 + 7 + 9 + 8 + 8
    return result


def get_x0_to_x9(dozens):
    length = len(dozens)
    result = (length * 10) + get_1_to_9()
    return result


def get_1_to_99():
    result = get_1_to_9() + get_10_to_19() + get_x0_to_x9("twenty") + get_x0_to_x9("thirty") + get_x0_to_x9("forty") + \
        get_x0_to_x9("fifty") + get_x0_to_x9("sixty") + get_x0_to_x9("seventy") + get_x0_to_x9("eighty") + get_x0_to_x9("ninety")
    return result


def get_x00_to_x99(hundreds):
    # 'hundred' = 7
    pure_hundred = len(hundreds) + 7

    # 'hundred and' = 10
    length = len(hundreds) + 10

    result = pure_hundred + (length * 99) + get_1_to_99()
    return result


def get_100_to_999():
    result = get_x00_to_x99("one") + get_x00_to_x99("two") + get_x00_to_x99("three") + get_x00_to_x99("four") + \
        get_x00_to_x99("five") + get_x00_to_x99("six") + get_x00_to_x99("seven") + get_x00_to_x99("eight") + get_x00_to_x99("nine")

    return result


def get_1_to_1000():
    # 'one thousand' = 11
    result = get_1_to_99() + get_100_to_999() + 11
    print(result)
    return result


# one       3
# two       3
# three     5
# four      4
# five      4
# six       3
# seven     5
# eight     5
# nine      4
# ten       3
# eleven    6
# twelve    6
# thirteen  8
# fourteen  8
# fifteen   7
# sixteen   7
# seventeen 9
# eighteen  8
# nineteen  8
# twenty    6
# thirty    6
# forty     5
# fifty     5
# sixty     5
# seventy   7
# eighty    6
# ninety    6

get_1_to_1000()
