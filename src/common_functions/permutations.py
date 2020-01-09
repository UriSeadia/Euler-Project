def is_permutation(a: int, b: int) -> bool:
    return ''.join(sorted(str(a))) == ''.join(sorted(str(b)))
