# You are given the following information, but you may prefer to do some research for yourself.
#
# 1 - 1.1.1900 was a Monday
# 2 - 30 days in April, June, September and November
# 3 - 31 days in January, March, May, July, August, October and December
# 4 - February has 28 days, and on leap years - 29
# 5 - A leap year occurs on any year evenly divisible by 4, but not on a century unless it is divisible by 400.

# How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?

from enum import IntEnum


class Days(IntEnum):
    SUNDAY = 1
    MONDAY = 2
    TUESDAY = 3
    WEDNESDAY = 4
    THURSDAY = 5
    FRIDAY = 6
    SATURDAY = 7


class Months(IntEnum):
    JANUARY = 1
    FEBRUARY = 2
    MARCH = 3
    APRIL = 4
    MAY = 5
    JUNE = 6
    JULY = 7
    AUGUST = 8
    SEPTEMBER = 9
    OCTOBER = 10
    NOVEMBER = 11
    DECEMBER = 12


def get_days_to_add(month, year):
    if month in [Months.APRIL, Months.JUNE, Months.SEPTEMBER, Months.NOVEMBER]:
        return 30

    if month in [Months.JANUARY, Months.MARCH, Months.MAY, Months.JULY, Months.AUGUST, Months.OCTOBER, Months.DECEMBER]:
        return 31

    if (year % 4) != 0:
        return 28

    if ((year % 100) == 0) and ((year % 400) != 0):
        return 28

    return 29


def count_sundays():
    day = Days.TUESDAY
    month = Months.JANUARY
    year = 1901
    counter = 0

    while year < 2001:
        days_to_add = get_days_to_add(month, year)
        day = (day + days_to_add) % 7

        if day == Days.SUNDAY:
            counter += 1

        if month == Months.DECEMBER:
            month = Months.JANUARY
            year += 1
        else:
            month += 1
    print(counter)


count_sundays()
