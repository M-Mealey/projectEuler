"""
Project Euler Problem 19
========================

You are given the following information, but you may prefer to do some
research for yourself.

  * 1 Jan 1900 was a Monday.
  * Thirty days has September,
    April, June and November.
    All the rest have thirty-one,
    Saving February alone,
    Which has twenty-eight, rain or shine.
    And on leap years, twenty-nine.
  * A leap year occurs on any year evenly divisible by 4, but not on a
    century unless it is divisible by 400.

How many Sundays fell on the first of the month during the twentieth
century (1 Jan 1901 to 31 Dec 2000)?
"""

# days in each month for both a normal year and a leap year
days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
days_leap_year = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

# first_day tracks what day of the week the first of the month was on. 0 = Sun, 1 = Mon, etc.
first_day = 2 # Jan 1st, 1901 was a tuesday

# running count of how many "Sunday the 1st"s have been found
sunday_1st_count = 0

for year in range(1901, 2001):
    # check if leap year
    days_per_month = days
    if year%4 == 0:
        days_per_month = days_leap_year
    # iterate over months, checking what day the 1st is on for each
    for m in days_per_month:
        next_first = (first_day + m) % 7
        if next_first == 0:
            sunday_1st_count += 1
        first_day = next_first

print(sunday_1st_count)

