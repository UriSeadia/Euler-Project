# A unit fraction contains 1 in the numerator.
# The decimal representation of the unit fractions with denominators 2 to 10 are given:
#
# 1/2	= 	0.5
# 1/3	= 	0.(3)
# 1/4	= 	0.25
# 1/5	= 	0.2
# 1/6	= 	0.1(6)
# 1/7	= 	0.(142857)
# 1/8	= 	0.125
# 1/9	= 	0.(1)
# 1/10	= 	0.1
# Where 0.1(6) means 0.166666..., and has a 1-digit recurring cycle.
#
# It can be seen that 1/7 has a 6-digit recurring cycle.
#
# Find the value of d < 1000 for which 1/d contains the longest recurring cycle in its decimal fraction part.


def get_cycle_length(numerator, denominator):
    remainder = numerator
    remainders = []
    i = 0

    while remainder > 0 and i < 1000000:
        if remainder < denominator:
            remainder *= 10
        else:
            remainder = remainder % denominator

            if remainder == 0:
                return 0

            if remainder in remainders:
                return len(remainders)
            else:
                remainders.append(remainder)

            i += 1

    return 1000000


def get_number_with_longest_recurring_cycle():
    max_number_candidate = 1
    current_max_number = 0
    current_max_cycles = 0

    while max_number_candidate < 1000:
        max_cycles_candidate = get_cycle_length(1, max_number_candidate)

        if max_cycles_candidate > current_max_cycles:
            current_max_cycles = max_cycles_candidate
            current_max_number = max_number_candidate

        max_number_candidate += 1

    print(current_max_number, current_max_cycles)
    return current_max_number


get_number_with_longest_recurring_cycle()
