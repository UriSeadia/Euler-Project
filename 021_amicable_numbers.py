# Let d(n) be defined as the sum of proper divisors of n (numbers less than n which divide evenly into n).

# If d(a) = b and d(b) = a, where a ≠ b, then a and b are an amicable pair and each of a and b are called amicable numbers.
#
# For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110;
# therefore d(220) = 284. The proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.
#
# Evaluate the sum of all the amicable numbers under 10000.


def d(num):
    result = 0
    i = 1

    while i < num:
        if num % i == 0:
            result += i
        i += 1
    return result


def get_sum_of_all_amicable_numbers(limit):
    result = 0
    a = 1

    while a < limit:
        b = d(a)

        if a != b and d(b) == a:
            result += a

        a += 1

    print(result)
    return result


get_sum_of_all_amicable_numbers(10000)
