def is_prime(number: int) -> bool:
    if number <= 1:
        return False

    if number <= 3:
        return True

    if number % 2 == 0 or number % 3 == 0:
        return False

    i = 5
    while i * i <= number:
        if (number % i == 0) or (number % (i + 2) == 0):
            return False
        i = i + 6

    return True


def get_primes_list(from_number: int, to_number: int) -> list:
    list_of_primes = []
    for i in range(from_number, to_number + 1):
        if is_prime(i):
            list_of_primes.append(i)
    return list_of_primes
