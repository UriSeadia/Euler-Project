# Using names.txt (right click and 'Save Link/Target As...'), a 46K text file containing over 5000 first names,
# begin by sorting it into alphabetical order.
# Then working out the alphabetical value for each name, multiply this value by its alphabetical position in the list to obtain a name score.
#
# For example, when the list is sorted into alphabetical order, COLIN, which is worth 3 + 15 + 12 + 9 + 14 = 53, is the 938th name in the list.
# So, COLIN would obtain a score of 938 × 53 = 49714.
#
# What is the total of all the name scores in the file?


def get_names_as_list_from_file(path):
    names_file = open(path, 'r')

    names_list = names_file.read().replace('"', "").split(',')
    sorted_list = sorted(names_list)

    names_file.close()

    return sorted_list


def get_name_value(name):
    result = 0
    lowercase_name = name.lower()

    for char in lowercase_name:
        result += ord(char) - 96

    return result


def get_names_scores():
    path = '/home/uri/Documents/p022_names.txt'
    names_list = get_names_as_list_from_file(path)

    result = 0
    i = 0
    length = len(names_list)

    while i < length:
        result = result + ((i + 1) * get_name_value(names_list[i]))
        i += 1

    print(result)


get_names_scores()
