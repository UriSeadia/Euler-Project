# Starting in the top left corner of a 2×2 grid, and only being able to move to the right and down,
# there are exactly 6 routes to the bottom right corner.
#
# How many such routes are there through a 20×20 grid?


def get_factorial(num):
    if num < 2:
        return 1

    return num * get_factorial(num - 1)


# The number of lattice paths from (0, 0) to (n, k) is ((n + k)!) / (n! * k!)
def get_number_of_lattice_paths(height, width):
    upper = get_factorial(height + width)
    lower = get_factorial(height) * get_factorial(width)
    result = upper / lower

    print(result)
    return result


get_number_of_lattice_paths(20, 20)
