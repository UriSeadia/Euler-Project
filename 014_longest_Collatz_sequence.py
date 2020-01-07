# The following iterative sequence is defined for the set of positive integers:
#
# n → n / 2 (n is even)
# n → 3n + 1 (n is odd)
#
# Using the rule above and starting with 13, we generate the following sequence:
#
# 13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1
# It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms.
# Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.
#
# Which starting number, under one million, produces the longest chain?
#
# NOTE: Once the chain starts the terms are allowed to go above one million.


def longest_collatz_sequence():
    max_terms = 0
    max_candidate_terms = 1
    max_number = 0

    current_number = 2

    while current_number < 1000000:
        running_number = current_number

        while running_number != 1:
            if running_number % 2 == 0:
                running_number /= 2
            else:
                running_number = (3 * running_number) + 1

            max_candidate_terms += 1

        if max_candidate_terms > max_terms:
            max_terms = max_candidate_terms
            max_number = current_number

        max_candidate_terms = 0
        current_number += 1

    print(max_number)
    print(max_terms)
    return max_number


longest_collatz_sequence()
