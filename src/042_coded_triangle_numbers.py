# The n-th term of the sequence of triangle numbers is given by, tn = ½n(n + 1); so the first 10 triangle numbers are:
# 1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...
#
# By converting each letter in a word to a number corresponding to its alphabetical position and adding these values we form a word value.
# For example, the word value for SKY is 19 + 11 + 25 = 55 = t10.
#
# If the word value is a triangle number then we shall call the word a triangle word.
#
# Using words.txt, containing nearly 2000 common English words, how many are triangle words?

import time


def get_triangle_list():
    t_list = []

    for i in range(1, 30):
        tn = int((0.5 * i) * (i + 1))
        t_list.append(tn)

    return t_list


def get_char_value(char: str):
    return ord(char.lower()) - (ord('a')) + 1


def get_word_value(word: str):
    value = 0

    for i in range(0, len(word)):
        value += get_char_value(word[i])

    return value


def get_words_as_list_from_file(path):
    words_file = open(path, 'r')

    words_list = words_file.read().replace('"', "").split(',')

    words_file.close()

    return words_list


def coded_triangle_numbers():
    words_list = get_words_as_list_from_file('/home/uri/Documents/p042_words.txt')
    triangle_words_count = 0
    triangle_list = get_triangle_list()

    for word in words_list:
        word_value = get_word_value(word)

        if word_value in triangle_list:
            triangle_words_count += 1

    return triangle_words_count


def main():
    start = time.time()

    print(coded_triangle_numbers())

    end = time.time()
    print('Seconds: ' + str(end - start))


main()
