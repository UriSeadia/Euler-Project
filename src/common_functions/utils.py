def is_pentagonal(num: int) -> bool:
    p = (((24 * num + 1) ** 0.5) + 1) / 6
    return p.is_integer()


def is_triangle(num: int) -> bool:
    t = (((8 * num + 1) ** 0.5) - 1) / 2
    return t.is_integer()


def is_hexagonal(num: int) -> bool:
    h = (((8 * num + 1) ** 0.5) + 1) / 4
    return h.is_integer()
