# In England the currency is made up of pound (£) and pence (p) and there are 8 coins in general circulation:
# 1p, 2p, 5p, 10p, 20p, 50p, £1 (100p) and £2 (200p).

# It is possible to make £2 in the following way:
# (1 * £1) + (1 * 50p) + (2 * 20p) + (1 * 5p) + (1 * 2p) + (3 * 1p)

# How many different ways can £2 be made using any number of coins?

from enum import IntEnum
import time


class Coins(IntEnum):
    ONE_PENNY = 1
    TWO_PENNIES = 2
    FIVE_PENNIES = 5
    TEN_PENNIES = 10
    TWENTY_PENNIES = 20
    FIFTY_PENNIES = 50
    ONE_POUND = 100
    TWO_POUNDS = 200


def get_coins_sum(two_pounds, one_pound, fifty_pennies, twenty_pennies, ten_pennies, five_pennies, two_pennies, one_penny):
    return (two_pounds * Coins.TWO_POUNDS) + \
           (one_pound * Coins.ONE_POUND) + \
           (fifty_pennies * Coins.FIFTY_PENNIES) + \
           (twenty_pennies * Coins.TWENTY_PENNIES) + \
           (ten_pennies * Coins.TEN_PENNIES) + \
           (five_pennies * Coins.FIVE_PENNIES) + \
           (two_pennies * Coins.TWO_PENNIES) + \
           (one_penny * Coins.ONE_PENNY)


def count_2_pound_ways():

    two_pounds, one_pound, fifty_pennies, twenty_pennies, ten_pennies, five_pennies, two_pennies, one_penny = 0, 0, 0, 0, 0, 0, 0, 0
    max_one_pound = Coins.TWO_POUNDS / Coins.ONE_POUND
    max_fifty_pennies = Coins.TWO_POUNDS / Coins.FIFTY_PENNIES
    max_twenty_pennies = Coins.TWO_POUNDS / Coins.TWENTY_PENNIES
    max_ten_pennies = Coins.TWO_POUNDS / Coins.TEN_PENNIES
    max_five_pennies = Coins.TWO_POUNDS / Coins.FIVE_PENNIES
    max_two_pennies = Coins.TWO_POUNDS / Coins.TWO_PENNIES
    max_one_penny = Coins.TWO_POUNDS / Coins.ONE_PENNY

    counter = 8

    while one_pound < max_one_pound:
        while fifty_pennies < max_fifty_pennies:
            while twenty_pennies < max_twenty_pennies:
                while ten_pennies < max_ten_pennies:
                    while five_pennies < max_five_pennies:
                        while two_pennies < max_two_pennies:
                            while one_penny < max_one_penny:
                                coins_sum = get_coins_sum(two_pounds, one_pound, fifty_pennies, twenty_pennies, ten_pennies, five_pennies, two_pennies, one_penny)

                                if coins_sum >= Coins.TWO_POUNDS:
                                    if coins_sum == Coins.TWO_POUNDS:
                                        print(two_pounds, one_pound, fifty_pennies, twenty_pennies, ten_pennies, five_pennies, two_pennies, one_penny, coins_sum)
                                        counter += 1
                                    break
                                one_penny += 1
                            one_penny = 0
                            two_pennies += 1
                        two_pennies = 0
                        five_pennies += 1
                    five_pennies = 0
                    ten_pennies += 1
                ten_pennies = 0
                twenty_pennies += 1
            twenty_pennies = 0
            fifty_pennies += 1
        fifty_pennies = 0
        one_pound += 1

    print(counter)
    return counter


# count_2_pound_ways()


# Other (Amazing...) solution
def efficient_count_2_pound_ways():
    start = time.time()

    amount = 200
    coins = [1, 2, 5, 10, 20, 50, 100, 200]
    answers = [1] + [0] * amount

    for coin in coins:
        for i in range(coin, amount + 1):
            answers[i] += answers[i - coin]

    print(answers[amount])

    end = time.time()
    print('Calculated in ' + str(end - start) + ' seconds.')


efficient_count_2_pound_ways()
